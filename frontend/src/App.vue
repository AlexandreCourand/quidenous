<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { fetchRandomQuestion, resetQuestions } from './api'

const question = ref('')
const remaining = ref(0)
const total = ref(0)
const loading = ref(false)
const started = ref(false)

async function nextQuestion() {
  loading.value = true
  try {
    const data = await fetchRandomQuestion()
    question.value = data.question
    remaining.value = data.remaining
    total.value = data.total
    started.value = true
  } finally {
    loading.value = false
  }
}

async function restart() {
  await resetQuestions()
  question.value = ''
  remaining.value = 0
  started.value = false
}

onMounted(() => {
  resetQuestions()
})
</script>

<template>
  <div class="app">
    <header>
      <h1>Qui de nous ?</h1>
      <p class="subtitle">Le jeu ou tout le monde est concerne</p>
    </header>

    <main>
      <div v-if="!started" class="welcome">
        <p class="instructions">
          Rassemblez-vous, tirez une question et debattez !
        </p>
        <button class="btn primary" :disabled="loading" @click="nextQuestion">
          C'est parti !
        </button>
      </div>

      <div v-else class="game">
        <div class="card">
          <p class="question">{{ question }}</p>
        </div>

        <div class="controls">
          <button
            v-if="remaining > 0"
            class="btn primary"
            :disabled="loading"
            @click="nextQuestion"
          >
            Suivante
          </button>

          <button v-else class="btn primary" @click="restart">
            Recommencer
          </button>
        </div>

        <p class="counter">{{ total - remaining }} / {{ total }}</p>
      </div>
    </main>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family:
    'Segoe UI',
    system-ui,
    -apple-system,
    sans-serif;
  background: #1a1a2e;
  color: #eee;
  min-height: 100vh;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

header {
  text-align: center;
  margin-bottom: 3rem;
}

h1 {
  font-size: 2.5rem;
  background: linear-gradient(135deg, #e94560, #0f3460);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  color: #888;
  margin-top: 0.5rem;
  font-style: italic;
}

.welcome {
  text-align: center;
}

.instructions {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #aaa;
}

.card {
  background: linear-gradient(135deg, #16213e, #0f3460);
  border: 1px solid #e94560;
  border-radius: 1rem;
  padding: 2.5rem;
  max-width: 500px;
  min-height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 32px rgba(233, 69, 96, 0.2);
}

.question {
  font-size: 1.4rem;
  text-align: center;
  line-height: 1.6;
}

.controls {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn {
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 0.5rem;
  font-size: 1.1rem;
  cursor: pointer;
  transition: transform 0.15s ease;
}

.btn:hover:not(:disabled) {
  transform: scale(1.05);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn.primary {
  background: linear-gradient(135deg, #e94560, #c23152);
  color: white;
}

.counter {
  margin-top: 1.5rem;
  text-align: center;
  color: #666;
  font-size: 0.9rem;
}
</style>
