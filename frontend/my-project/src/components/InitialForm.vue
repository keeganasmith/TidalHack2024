<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router';
    let result = {"Size_Class" : "","Curb_Wgt": 0.0,"ABS" : false,"Airbag_D" : false,"SSF" : 0.0,"Drive":"RWD","TireSize":0.0,"StabilityControl":false,
    "BrakeAssist":false,"TractionControl":false,"AdjUpperBeltFront":false,"AdjUpperBeltRear":false,"Pretensioner":false,"IntegratedSeat":false,"RearCtrLapShldrBelt":false,
    "AdvanceAirbagFeature":false,"SideAirbag":false,"HeadAirbag":false,"HeadAirbagRollover":false,
    "RearSeatHeadRestraint":false,"DynamicHeadRestraint":false,"Roll_Stability": false,"SafetyPowerWindows": false,"WheelsDriven":0}
    let check_box_options = ["ABS","Airbag_D","StabilityControl","BrakeAssist","TractionControl","AdjUpperBeltFront","AdjUpperBeltRear","Pretensioner","IntegratedSeat",
    "RearCtrLapShldrBelt","AdvanceAirbagFeature","SideAirbag","HeadAirbag","HeadAirbagRollover",
    "RearSeatHeadRestraint","DynamicHeadRestraint","Roll_Stability","SafetyPowerWindows"]
    const check_box_labels = ["Has ABS", "Has front airbags", "Has stability control - ESC", "Has brake assist", "Has traction control", "Has adjustable upperbelt - front",
    "Has Adjustable upperbelt - rear", "Has pretensioner", "Has integrated safety belt system", "Has rear center lap/shoulder belts", "Has advanced frontal airbag feature", "Has side airbag", 
    "Has head airbag", "Has rear seat head restraint", "Has dynamic head restraint", "Has roll stability control", "Has safety power windows"]
    const class_options =["Sport Utility Vehicle", 'Compact Passenger Car', 'Pickup', 'Van',
 'Medium Passenger Car', 'Heavy Passenger Car' ,'Light Passenger Car',
 'Mini Passenger Car']
    const drive_options = ["4X2 FWD", "4X2 RWD", "4X4 4WD", "4X4 AWD"]
    const router = useRouter();
    const check_box_value = ref([])
    function handleSubmit(values){
        for(let i = 0; i < check_box_value.value.length; i++){
            let check_box_label = check_box_value.value[i]
            console.log(check_box_label)
            for(let j =0 ; j < check_box_labels.length; j++){
                if(check_box_label === check_box_labels[j]){
                    result[check_box_options[j]] = true;
                    break;
                }
            }
        }
        let keys = Object.keys(values)
        for(let i = 0; i < keys.length; i++){
            if(keys[i] === "ignore"){
                continue
            }
            result[keys[i]] = values[keys[i]]
        }
        let drive_option = values["Drive_type"]
        delete result["Drive_type"]
        if(drive_option === "4X2 FWD"){
            result["Drive"] = "FWD"
            result["WheelsDriven"] = "FWD"
        }
        else if(drive_option === "4X2 RWD"){
            result["Drive"] = "RWD"
            result["WheelsDriven"] = "RWD"
        }
        else if(drive_option === "4X4 4WD"){
            result["Drive"] = "4WD"
            result["WheelsDriven"] = "4WD"
        }
        else{
            result["Drive"] = "AWD"
            result["WheelsDriven"] = "AWD"
        }
        sessionStorage.setItem('submissionInfo', JSON.stringify(result));
        router.push({
        name: 'submission' // Name of the route
        });

    }
</script>


<template>
    <div style="background-color: white; color: black; padding: 20px;">
      <h3 style="color: green;">Please enter the characteristics of the vehicle you would like to test</h3>
      <FormKit
        type="form"
        @submit="handleSubmit"
        style="border: 2px solid green; padding: 20px; border-radius: 10px;"
      >
        <FormKit
          name="ignore"
          v-model="check_box_value"
          type="checkbox"
          label="Safety features"
          :options="check_box_labels"
          label-class="form-label"
        />
        <FormKit
          name="Size_Class"
          type="select"
          label="Choose a vehicle class:"
          :options="class_options"
          label-class="form-label"
        />
        <FormKit
          name="Curb_Wgt"
          label="Enter the curb weight of the vehicle (lbs):"
          type="number"
          step="0.01"
          label-class="form-label"
        />
        <FormKit
          name="SSF"
          label="Please enter the static stability factor:"
          type="number"
          step="0.01"
          label-class="form-label"
        />
        <FormKit
          name="TireSize"
          label="Please enter the diameter of the tires in inches:"
          type="number"
          step="0.01"
          label-class="form-label"
        />
        <FormKit
          name="Drive_type"
          type="select"
          label="Choose a drive type:"
          :options="drive_options"
          label-class="form-label"
        />
        <!-- Add a submit button -->
        
        
      </FormKit>
    </div>
  </template>
  
  <style>
  .form-label {
    color: black;
    margin-bottom: 5px;
    font-weight: bold;
  }
  </style>