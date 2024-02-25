<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();

let endpoint = "https://tidalhack2024.onrender.com/get_score";
let isLoading = ref(true);
let score = ref(null); 
let drstar = ref(null);
let drsstar = ref(null);
let pastar = ref(null);
let passtar = ref(null);
function handleBack(){
    router.push({
        name: 'initialForm' // Name of the route
    });
}
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
    <div style="color: black; padding: 20px;">
        <button 
            @click="handleBack" 
            style="background-color: green; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 20px;">
            Back
        </button>
        <div v-if="isLoading" style="color: green; font-weight: bold;">
            Loading...
        </div>
        <div v-else>
            <h3 style="color: green;">Predicted Crash Test Ratings</h3>
            <ul>
                <li style="margin-bottom: 10px;">Frontal Impact Driver Star rating: <span style="font-weight: bold;">{{ drstar }} / 5</span></li>
                <li style="margin-bottom: 10px;">Frontal Impact Passenger Star rating: <span style="font-weight: bold;">{{ pastar }} / 5</span></li>
                <li style="margin-bottom: 10px;">Side Impact Rear Seat Driver Star rating: <span style="font-weight: bold;">{{ drsstar }} / 5</span></li>
                <li style="margin-bottom: 10px;">Side Impact Rear Seat Passenger Star rating: <span style="font-weight: bold;">{{ passtar }} / 5</span></li>
            </ul>
        </div>
    </div>
</template>
