<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';

import ChannelsList from './components/Chat/ChannelsList.vue';
import MembersList from './components/Chat/MembersList.vue';
import MessageChannel from './components/Chat/MessageChannel.vue';

const route = useRoute();
const groupId = ref(route.params.group_id)

const channels = [
  { id: 1, name: 'general' },
  { id: 2, name: 'random' },
];

const selectedChannel = ref(1);

const messages = ref([
  {
    id: 1,
    channel: 1,
    user: 'User1',
    avatar: 'https://ui-avatars.com/api/?name=U1&background=dedede&color=888',
    time: '10:30 AM',
    content: 'Hello there! 👋',
  },
  {
    id: 2,
    channel: 1,
    user: 'User2',
    avatar: 'https://ui-avatars.com/api/?name=U2&background=dedede&color=888',
    time: '10:32 AM',
    content: "Hey! What's up?",
  },
  {
    id: 3,
    channel: 2,
    user: 'User1',
    avatar: 'https://ui-avatars.com/api/?name=U1&background=dedede&color=888',
    time: '11:00 AM',
    content: 'Random things!',
  },
]);

const filteredMessages = computed(() =>
  messages.value.filter(msg => msg.channel === selectedChannel.value)
);

// Example members list
const members = [
  {
    id: 1,
    name: 'User1',
    avatar: 'https://ui-avatars.com/api/?name=U1&background=dedede&color=888',
    status: 'online',
  },
  {
    id: 2,
    name: 'User2',
    avatar: 'https://ui-avatars.com/api/?name=U2&background=dedede&color=888',
    status: 'offline',
  },
  {
    id: 3,
    name: 'You',
    avatar: 'https://ui-avatars.com/api/?name=You&background=dedede&color=888',
    status: 'online',
  },
];
</script>

<template>
  <div class="flex h-screen bg-gray-50">
    <!-- Channel List (Left) -->
    <aside class="w-60 bg-white border-r border-gray-200 flex flex-col" aria-label="channel list">
      <div class="flex items-center h-16 px-6 border-b border-gray-200">
        <h2 class="text-2xl font-bold text-gray-900">Group Name</h2>
      </div>
      <ChannelsList :channels="channels" v-model="selectedChannel"></ChannelsList>
    </aside>
    <!-- Chat Section -->
    <main class="flex-1 flex flex-col">
      <MessageChannel :channel="channels.find(c => c.id === selectedChannel)" :messages="filteredMessages"></MessageChannel>
    </main>
    <!-- Members List (Right) -->
    <aside class="w-64 bg-white border-l border-gray-200 flex flex-col" aria-label="member list">
      <div class="flex items-center h-16 px-6 border-b border-gray-200">
        <span class="text-xl font-semibold text-gray-900">Members - {{ members.length }}</span>
      </div>
      <MembersList :members="members"></MembersList>
    </aside>
  </div>
</template>
