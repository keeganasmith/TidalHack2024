<script>
import { defineComponent } from 'vue';

export default defineComponent({
    props: {
        route: Object,
        selected: Boolean
    }

})
</script>

<template>
    <li :style="{ color: selected ? 'blue' : 'black' }" @click="handleClick">
        {{ route["safety"] }}
    </li>
</template>