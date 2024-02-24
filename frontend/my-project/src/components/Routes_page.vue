<template>
    <h1>this is the page that will show the other map w/ possible routes</h1>
</template>

<script>
import { defineComponent } from "vue";
// import { GoogleMap, Marker } from "vue3-google-map";
export default defineComponent({
    // components: { GoogleMap, Marker },
    props: { routes : Array},
    setup() {
        //const center = { lat: 40.689247, lng: -74.044502 };
        const my_key = process.env.VUE_APP_GOOGLE_MAPS_API_KEY
        return { my_key };
    },
    data() {
        return {
            selected_route: 0,
        }
    }

})
</script>