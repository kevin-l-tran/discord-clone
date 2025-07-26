<script setup lang="ts">
defineProps({
    groupImage: String,
    groupName: String
});
</script>

<template>
    <div
        class="w-72 bg-white shadow-lg border-3 border-white rounded-xl overflow-hidden cursor-pointer transition duration-500 hover:shadow-xl hover:border-sky-300 hover:shadow-xl">
        <img :src="groupImage" alt="Group" class="w-full h-40 object-cover" />
        <div class="p-4">
            <h2 class="text-xl font-extrabold text-gray-800">
                {{ groupName }}
            </h2>
        </div>
    </div>
</template>