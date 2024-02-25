<script setup>
import { defineProps } from 'vue';

defineProps({
    form_results: {
        type: Array,
        default: () => []
    }
});
let joe = sessionStorage.getItem('submissionInfo');
</script>

<template>
    <div>
        <h3>You Submitted:</h3>
        <p> {{ joe }}</p>
    </div>
</template>