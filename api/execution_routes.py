import logging
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from database.task_repository import TaskRepository
from services.execution_service import (
    ExecutionService,
    TaskNotFoundError,
    StepNotFoundError,
    DependencyViolationError,
    InvalidStatusTransitionError
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/execution", tags=["Execution"])
execution_service = ExecutionService()

@router.get("/{task_id}")
async def get_execution_state(task_id: str):
    try:
        if not ObjectId.is_valid(task_id):
            raise HTTPException(status_code=400, detail="Invalid ObjectId")
            
        task = TaskRepository.get_task(ObjectId(task_id))
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
            
        logger.info(f"Execution state loaded: {task_id}")
        
        return {
            "task_id": str(task.get("_id")),
            "status": task.get("status", "unknown"),
            "analysis": task.get("analysis", {}),
            "execution_plan": task.get("execution_plan", {}),
            "progress": task.get("progress", {}),
            "emergency_mode": task.get("emergency_mode", {})
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"API error getting execution state {task_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{task_id}/start-step/{step_id}")
async def start_step(task_id: str, step_id: str):
    try:
        updated_task = execution_service.start_step(task_id, step_id)
        logger.info(f"Step started: {step_id} for task: {task_id}")
        
        # Convert ObjectId to string for JSON serialization
        if "_id" in updated_task:
            updated_task["_id"] = str(updated_task["_id"])
            
        return updated_task
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except StepNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except DependencyViolationError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except InvalidStatusTransitionError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        logger.error(f"API error starting step {step_id} for task {task_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{task_id}/complete-step/{step_id}")
async def complete_step(task_id: str, step_id: str):
    try:
        updated_task = execution_service.complete_step(task_id, step_id)
        logger.info(f"Step completed: {step_id} for task: {task_id}")
        
        # Convert ObjectId to string for JSON serialization
        if "_id" in updated_task:
            updated_task["_id"] = str(updated_task["_id"])
            
        return updated_task
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except StepNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except InvalidStatusTransitionError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        logger.error(f"API error completing step {step_id} for task {task_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{task_id}/reopen-step/{step_id}")
async def reopen_step(task_id: str, step_id: str):
    try:
        updated_task = execution_service.reopen_step(task_id, step_id)
        logger.info(f"Step reopened: {step_id} for task: {task_id}")
        
        # Convert ObjectId to string for JSON serialization
        if "_id" in updated_task:
            updated_task["_id"] = str(updated_task["_id"])
            
        return updated_task
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except StepNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except InvalidStatusTransitionError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        logger.error(f"API error reopening step {step_id} for task {task_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
