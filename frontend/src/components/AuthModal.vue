<script setup lang="ts">
import { ref, defineEmits } from 'vue'

const emit = defineEmits(['close'])

const isSignUp = ref(false)

function toggle() {
  isSignUp.value = !isSignUp.value
}
</script>

<template>
  <Transition enter-from-class="opacity-0 scale-75" enter-to-class="opacity-100 scale-100"
    enter-active-class="transition duration-200" leave-from-class="opacity-100" leave-to-class="opacity-0"
    leave-active-class="transition duration-200 ">
    <!-- backdrop -->
    <div class="fixed inset-0 flex items-center justify-center z-50" @click="$emit('close')">
      <!-- modal box -->
      <div class="relative w-[720px] h-[480px] bg-white rounded-xl overflow-hidden shadow-xl" @click.stop>

        <!-- static forms side-by-side (full modal) -->
        <div class="absolute inset-0 flex">
          <!-- Sign In form -->
          <form class="w-1/2 h-full flex flex-col items-center justify-center p-8">
            <h1 class="text-3xl font-bold mb-4">Sign In</h1>
            <input type="username" placeholder="Username"
              class="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sky-400" />
            <input type="password" placeholder="Password"
              class="w-full mb-2 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sky-400" />
            <a href="#" class="self-end text-sm text-gray-500 hover:underline mb-6">Forgot your password?</a>
            <button
              class="cursor-pointer w-full py-3 bg-indigo-600 text-white font-semibold rounded-md hover:bg-indigo-800 transition-colors duration-500">
              Sign In
            </button>
          </form>

          <!-- Sign Up form -->
          <form class="w-1/2 h-full flex flex-col items-center justify-center p-8">
            <h2 class="text-3xl font-bold mb-4">Create Account</h2>
            <input type="email" placeholder="Email"
              class="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sky-400" />
            <input type="text" placeholder="Username"
              class="w-full mb-1 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sky-400" />
            <div class="text-xs self-end text-gray-500">Username must be over 3 characters long.</div>
            <input type="password" placeholder="Password"
              class="w-full mb-1 mt-3 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sky-400" />
            <div class="text-xs self-end text-gray-500 mb-5">Password must be over 7 characters long.</div>
            <button
              class="cursor-pointer w-full py-3 bg-indigo-600 text-white font-semibold rounded-md hover:bg-indigo-800 transition-colors duration-500">
              Sign Up
            </button>
          </form>
        </div>

        <!-- overlay panel (slides left/right over forms) -->
        <div
          class="absolute top-0 right-0 w-1/2 h-full flex flex-col items-center justify-center px-8 text-white bg-gradient-to-r from-indigo-950 to-indigo-900 transition-transform duration-700 z-10"
          :class="isSignUp ? '-translate-x-full' : 'translate-x-0'">
          <h2 class="text-3xl font-bold mb-2">
            {{ isSignUp ? 'Welcome Back!' : 'Hello, Friend!' }}
          </h2>
          <p class="text-center mb-6">
            {{ isSignUp
              ? 'To keep connected with us, login with your personal info!'
              : 'Enter your personal details and start your journey with us!' }}
          </p>
          <button @click="toggle"
            class="cursor-pointer mt-2 px-6 py-2 border-2 border-white rounded-full uppercase text-sm font-medium hover:bg-white hover:text-sky-500 transition-colors duration-500">
            {{ isSignUp ? 'Sign In' : 'Sign Up' }}
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>
