import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue'
import InitialForm from './components/InitialForm.vue'

const routes = [
    { path: '/', component: InitialForm },
];
  
const router = createRouter({
    history: createWebHistory(),
    routes
});
const app = createApp(App)
app.use(router)
app.mount('#app')
