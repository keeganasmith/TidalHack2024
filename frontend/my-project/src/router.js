import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import Routes_page from './components/Routes_page.vue';


const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/routes', name: 'RoutesPage', component: Routes_page },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
