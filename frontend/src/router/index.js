import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import NewText from '../views/NewText.vue'
import Text from '../views/Text.vue'
import Sentence from '../views/Sentence.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/new',
    component: NewText
  },
      {
    path: '/text/:textId',
    component: Text,
    props: true
  },
      {
    path: '/sentence/:sentenceId',
    component: Sentence,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
