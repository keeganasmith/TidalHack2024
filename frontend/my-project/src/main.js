import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue'
import InitialForm from './components/InitialForm.vue'
import Submission from './components/SubmissionPage.vue'
import { plugin, defaultConfig } from '@formkit/vue'
const routes = [
    { path: '/', name: "initialForm", component: InitialForm },
    { path: '/submission', name: "submission", component: Submission}
];
  
const router = createRouter({
    history: createWebHistory(),
    routes
});
const app = createApp(App)
app.use(router)
app.use(plugin, defaultConfig)
app.mount('#app')
