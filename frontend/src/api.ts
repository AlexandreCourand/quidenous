export interface QuestionResponse {
  question: string
  remaining: number
  total: number
}

export async function fetchRandomQuestion(): Promise<QuestionResponse> {
  const response = await fetch('/api/question/random')
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`)
  }
  return response.json()
}

export async function resetQuestions(): Promise<void> {
  const response = await fetch('/api/question/reset')
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`)
  }
}
