import { describe, it, expect, vi, beforeEach } from 'vitest'
import { mount, flushPromises } from '@vue/test-utils'
import App from '../App.vue'

const mockQuestion = {
  question: 'Qui est le plus drole ?',
  remaining: 29,
  total: 30,
}

beforeEach(() => {
  vi.stubGlobal(
    'fetch',
    vi.fn().mockResolvedValue({
      ok: true,
      json: () => Promise.resolve(mockQuestion),
    }),
  )
})

describe('App', () => {
  it('renders welcome screen initially', () => {
    const wrapper = mount(App)
    expect(wrapper.text()).toContain('Qui de nous ?')
    expect(wrapper.text()).toContain("C'est parti")
  })

  it('shows question after clicking start', async () => {
    const wrapper = mount(App)
    await wrapper.find('.btn.primary').trigger('click')
    await flushPromises()
    expect(wrapper.text()).toContain('Qui est le plus drole ?')
    expect(wrapper.text()).toContain('Suivante')
  })
})
