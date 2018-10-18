import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Movies from '@/components/Movies';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Movies',
      component: Movies,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'hash',
});
