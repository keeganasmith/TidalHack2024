<script setup>
import { ref, onMounted } from 'vue';

let endpoint = "http://localhost:5000/get_score";
let isLoading = ref(true);
let score = ref(null); 

async function fetchScore() {
    let joe = sessionStorage.getItem('submissionInfo');
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: joe,
        });
        const data = await response.json(); 
        score.value = data; 
    } catch (error) {
        console.error('Error fetching score:', error);
    } finally {
        isLoading.value = false; 
    }
}
onMounted(fetchScore);
</script>

<template>
    <div>
        <h3>You Submitted:</h3>
        <div v-if="isLoading">
            Loading...
        </div>
        <div v-else>
            <p>{{ score }}</p>
        </div>
    </div>
</template>
