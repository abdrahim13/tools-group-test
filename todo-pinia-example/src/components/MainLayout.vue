<template>
  <Layout>
    <LayoutHeader>
      <RouterLink class="link" to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </LayoutHeader>
    <LayoutContent class="content">
      <slot></slot>
    </LayoutContent>
  </Layout>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router';
import {
  Layout,
  LayoutHeader,
  LayoutContent,
} from 'ant-design-vue';
</script>

<style scoped>
.content {
  padding: 0.5rem 1rem;
  max-width: 800px;
  width: 95%;
  min-height: 100vh;
  margin: 1rem auto;
}
.link {
  margin-right: 15px;
}
</style>
