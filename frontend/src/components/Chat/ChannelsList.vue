<script setup>
defineProps({
  channels: {
    type: Array,
    default: () => []
  }
});

const modelValue = defineModel()
</script>

<template>
  <div class="flex-1 overflow-y-auto">
    <div class="px-3 py-2 text-xs text-gray-400 uppercase">Text Channels</div>
    <ul>
      <li v-for="channel in channels" :key="channel.id"
        :class="['flex items-center px-4 py-2 cursor-pointer rounded-lg mx-2 mb-1 transition', channel.id === modelValue ? 'bg-gray-100 text-indigo-700 font-semibold' : 'text-gray-700 hover:bg-gray-100']"
        @click="modelValue = channel.id">
        <span class="mr-2 text-lg">#</span>
        <span>{{ channel.name }}</span>
      </li>
    </ul>
  </div>
</template>