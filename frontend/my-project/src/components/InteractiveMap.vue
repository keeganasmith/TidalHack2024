<template>
  <div>
    <h1>hello</h1>
    <GoogleMap :api-key="my_key" style="width: 100%; height: 500px" :center="center" :zoom="15" @click = handleMapClick>
      <Marker :options="{ position: center }" />
    </GoogleMap>
    <button @click="HandleClick">Click Me!</button>
  </div>
</template>


<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

export default defineComponent({
  components: { GoogleMap, Marker },
  setup() {
    //const center = { lat: 40.689247, lng: -74.044502 };
    const my_key = process.env.VUE_APP_GOOGLE_MAPS_API_KEY
    return { my_key };
  },
  data(){
    return {
      center : {lat: 40.689247, lng: -74.044502 },
    }
  },
  methods: {
    getLocation(){
      navigator.geolocation.getCurrentPosition(
          this.showPosition,
          this.showError
      );
    },
    showPosition(position){
      this.center = {lat: position.coords.latitude, lng: position.coords.longitude}
    },
    handleMapClick(event){
      console.log("got here" + event)
      alert('Button clicked!');
    }
  },
  mounted() {
    this.getLocation();
  }
});
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

</style>