from typing import List
from fastapi import APIRouter, Response, status
from models.policy import Policy, PolicyBase, PolicyPut

router = APIRouter()
urlRoute = '/policy'
urlIdRoute = '/policy/{obj_id}'

policies: List[Policy] = []

@router.get(urlRoute, status_code=status.HTTP_200_OK)
def get_all_policy():
    return policies

@router.get(urlIdRoute, status_code=status.HTTP_200_OK)
def get_policy_by_id(obj_id: str, response: Response):
    for policy in policies:
        if str(policy.policy_id) == obj_id:
            return policy.model_dump()
    response.status_code = status.HTTP_204_NO_CONTENT
    return {}

@router.post(urlRoute, status_code=status.HTTP_201_CREATED)
async def create_policy(obj_model: PolicyBase):
    policy = Policy(**obj_model.model_dump())
    policies.append(policy)
    return policy.model_dump()

@router.put(urlIdRoute, status_code=status.HTTP_200_OK)
async def update_policy_by_id(obj_id:str, obj_model:PolicyPut):
    for policy in policies:
        if str(policy.policy_id) == obj_id:
            policy.customer_name = obj_model.customer_name or policy.customer_name 
            policy.policy_type = obj_model.policy_type or policy.policy_type
            policy.expiry_date = obj_model.expiry_date or policy.expiry_date
            return {'status': 'UPDATED'}
    return {'status': f'NO POLICY FOUND WITH ID {obj_id}'}

@router.delete(urlIdRoute, status_code=status.HTTP_200_OK)
async def delete_policy_by_id(obj_id:str):
    policies[:] = [p for p in policies if str(p.policy_id) != obj_id]
    return {'status': 'DELETED'}