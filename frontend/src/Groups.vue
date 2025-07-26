<script setup lang="ts">
import GroupCard from './components/Group/GroupCard.vue';

const tempGroups = [
  {
    id: 'advising',
    name: 'NSM College Advising',
    image: '/src/assets/background.avif',
  },
  {
    id: 'cpsc449',
    name: 'Summer 2025 CPSC 449',
    image: '/src/assets/background.avif',
  },
];
</script>

<template>
  <div class="p-6 bg-neutral-100 min-h-screen">
    <header class="m-8">
      <h1 class="text-6xl text-blue-950 font-black mb-6 pb-3 border-b-4 border-sky-500">Your Groups</h1>
    </header>

    <div class="flex flex-wrap gap-10 m-8">
      <GroupCard v-for="group in tempGroups" :key="group.id" :group-image="group.image" :group-name="group.name">
      </GroupCard>

      <div
        class="w-72 bg-white shadow-lg rounded-xl border-3 border-white overflow-hidden transition duration-500 hover:shadow-xl hover:border-sky-300 flex flex-col items-center justify-between">
        <button class="text-5xl font-semibold text-gray-800 hover:text-sky-600 transition cursor-pointer mt-8">
          + Add
        </button>
        <div class="w-64 h-1 bg-gray-300" />
        <button class="text-5xl font-semibold text-gray-800 hover:text-sky-600 transition cursor-pointer mb-8">
          + Create
        </button>
      </div>
    </div>
  </div>
</template>
