from database.task_repository import TaskRepository


class TaskListService:

    def get_tasks(self):

        tasks = TaskRepository.get_all_tasks()

        result = []

        for task in tasks:

            analysis = task.get("analysis") or {}
            progress = task.get("progress") or {}
            emergency = task.get("emergency_mode") or {}

            title = analysis.get("title")
            if not title:
                title = "Untitled Task"
                
            deadline = analysis.get("deadline") or "No deadline"
            last_updated = task.get("updated_at") or task.get("created_at") or "Unknown"
            created_at = task.get("created_at") or "Unknown"

            result.append({
                "id": str(task["_id"]),
                "title": title,
                "status": task.get("status", "unknown"),
                "progress": round(
                    progress.get("overall_completion", 0)
                ),
                "risk": emergency.get(
                    "risk_level",
                    "Safe"
                ),
                "deadline": deadline,
                "last_updated": last_updated,
                "created_at": created_at
            })

        return result