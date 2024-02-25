<script setup>
import { ref, onMounted } from 'vue';

let endpoint = "http://localhost:5000/get_score";
let isLoading = ref(true);
let score = ref(null); 
let drstar = ref(null);
let drsstar = ref(null);
let pastar = ref(null);
let passtar = ref(null);
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
        drstar.value = data["DrStar_Num"][0] + 1
        drsstar.value = data["DrSSTar_Num"][0] + 1
        pastar.value = data["PaStar_Num"][0] + 1
        passtar.value = data["PaSStar_Num"][0] + 1
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
            <ul>
                <li>Frontal Impact Driver Star rating: {{ drstar }} / 5</li>
                <li>Frontal Impact Passenger Star rating: {{ pastar }} / 5</li>
                <li>Side Impact Rear Seat Driver Star rating: {{ drsstar }} / 5</li>
                <li>Side Impact Rear Seat Passenger Star rating: {{ passtar }} / 5</li>
            </ul>
        </div>
    </div>
</template>
