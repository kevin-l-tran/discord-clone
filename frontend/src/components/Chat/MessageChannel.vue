<script setup lang="ts">
import { ref } from 'vue';

defineProps({
    channel: {
        type: Object
    },
});

const messages = ref([]);
</script>

<template>
    <!-- Header -->
    <header class="flex items-center h-16 px-6 bg-white border-b border-gray-200">
        <span class="text-xl font-bold text-gray-900"># {{ channel.name }}</span>
    </header>
    <!-- Chat Messages -->
    <section class="flex-1 overflow-y-auto px-6 py-4 bg-gray-50">
        <div v-for="msg in messages" :key="msg.id" class="flex items-start mb-6">
            <img :src="msg.avatar" alt="avatar"
                class="w-10 h-10 rounded-full mr-4 border border-gray-200 bg-gray-200" />
            <div>
                <div class="flex items-center mb-1">
                    <span class="font-semibold text-gray-900 mr-2">{{ msg.user }}</span>
                    <span class="text-xs text-gray-400">{{ msg.time }}</span>
                </div>
                <div class="text-gray-800 leading-relaxed">
                    <span v-html="msg.content"></span>
                </div>
            </div>
        </div>
    </section>
    <!-- Message Input -->
    <footer class="p-4 bg-white border-t border-gray-200">
        <div class="flex items-center bg-gray-100 rounded-xl px-4 py-2">
            <input
                class="flex-1 bg-transparent outline-none text-gray-900 placeholder-gray-500"
                :placeholder="`Message #${channel.name}`" />
            <button
                class="ml-3 px-3 py-1 rounded-lg bg-indigo-600 text-white font-semibold transition hover:bg-indigo-700">
                Send
            </button>
        </div>
    </footer>
</template>