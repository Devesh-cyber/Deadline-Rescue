export interface ActiveTask {
  title: string;
  deadline: string;
  assignee: string;
  progress: number;
  status: string;
}

export interface Milestone {
  id?: string;
  title: string;
  description: string;
  durationTracked: string;
  status: string;
  difficulty: string;
}

export interface UpcomingRisk {
  title: string;
  details: string;
  type: string;
}

export interface FocusTask {
  title: string;
  description: string;
  deadline: string;
  timeEst: string;
  difficulty: string;
  overallProgress: number;
}

export interface RescuePlan {
  taskId?: string;
  welcomeMessage: string;
  urgentRescuePointsCount: number;
  focusTask: FocusTask;
  insights: string[];
  upcomingRisks: UpcomingRisk[];
  confidenceScore: string;
  processingPriority: string;
  activeTasks: ActiveTask[];
  milestones: Milestone[];
}

export interface TaskListItem {
  id: string;
  title: string;
  status: string;
  progress: number;
  risk: string;
  deadline?: string;
  last_updated?: string;
  created_at?: string;
}

export interface Analysis {
  title: string;
  summary?: string;
  task_type?: string;
  deadline?: string;
  priority?: string;
  difficulty?: string;
  estimated_hours?: number;
  confidence?: number;
}

export interface Progress {
  overall_completion: number;
  completed_steps: number;
  remaining_steps: number;
  blocked_steps: number;
  current_phase: string;
  current_step: string;
  remaining_hours: number;
  completed_hours: number;
  next_available_steps: string[];
}

export interface ExecutionStep {
  step_id: string;
  title: string;
  description: string;
  estimated_hours?: number;
  status?: string;
  emergency_priority?: string;
  started_at?: string;
  completed_at?: string;
}

export interface ExecutionPhase {
  phase_id: string;
  title: string;
  description?: string;
  steps: ExecutionStep[];
}

export interface ExecutionPlan {
  total_estimated_hours?: number;
  critical_path?: string[];
  phases: ExecutionPhase[];
}

export interface EmergencyMode {
  risk_level: string;
  remaining_days?: number;
  remaining_hours?: number;
  remaining_estimated_hours?: number;
  overall_completion?: number;
  steps_to_skip?: string[];
  focus_steps?: string[];
  recommended_work_order?: string[];
  recovery_plan?: string[];
  generate_solution?: boolean;
}

export interface DashboardSummary {
  title: string;
  deadline: string;
  overall_completion: number;
  risk_level: string;
  current_step: string;
  remaining_hours: number;
}

export interface DashboardResponse {
  task_id: string;
  status: string;
  analysis: Analysis;
  progress: Progress;
  emergency_mode: EmergencyMode;
  summary: DashboardSummary;
}

export type ViewType =
  | "tasklist"
  | "upload"
  | "dashboard"
  | "execution"
  | "analyzing"
  | "settings";