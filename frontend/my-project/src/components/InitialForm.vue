<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router';
    let result = {"Size_Class" : "","Curb_Wgt": 0.0,"ABS" : false,"Airbag_Front" : false,"SSF" : 0.0,"Drive":false,"Drive4":false,"TireSize":0.0,"StabilityControl":false,
    "BrakeAssist":false,"TractionControl":false,"AdjUpperBeltFront":false,"AdjUpperBeltRear":false,"Pretensioner":false,"IntegratedSeat":false,"RearCtrLapShldrBelt":false,
    "AdvanceAirbagFeature":false,"SideAirbag":false,"HeadAirbag":false,"HeadAirbagRollover":false,
    "RearSeatHeadRestraint":false,"DynamicHeadRestraint":false,"BuiltInChildSeat":false,"Roll_Stability": false,"SafetyPowerWindows": false,"WheelsDriven":0}
    let check_box_options = ["ABS","Airbag_Front","StabilityControl","BrakeAssist","TractionControl","AdjUpperBeltFront","AdjUpperBeltRear","Pretensioner","IntegratedSeat",
    "RearCtrLapShldrBelt","AdvanceAirbagFeature","SideAirbag","HeadAirbag","HeadAirbagRollover",
    "RearSeatHeadRestraint","DynamicHeadRestraint","BuiltInChildSeat","Roll_Stability","SafetyPowerWindows"]
    const check_box_labels = ["Has ABS", "Has front airbags", "Has stability control - ESC", "Has brake assist", "Has traction control", "Has adjustable upperbelt - front",
    "Has Adjustable upperbelt - rear", "Has pretensioner", "Has integrated safety belt system", "Has rear center lap/shoulder belts", "Has advanced frontal airbag feature", "Has side airbag", 
    "Has head airbag", "Has rear seat head restraint", "Has dynamic head restraint", "Has builtin child seat", "Has roll stability control", "Has safety power windows"]
    const class_options =["Sport Utility Vehicle", "Compact Passenger Car"] 
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
            result["Drive4"] = ""
        }
        else if(drive_option === "4X2 RWD"){
            result["Drive"] = "RWD"
            result["Drive4"] = ""
        }
        else if(drive_option === "4X4 4WD"){
            result["Drive"] = ""
            result["Drive4"] = "4WD"
        }
        else{
            result["Drive"] = ""
            result["Drive4"] = "AWD"
        }
        sessionStorage.setItem('submissionInfo', JSON.stringify(result));
        router.push({
        name: 'submission' // Name of the route
        });

    }
</script>


<template>
    <FormKit 
    type="form"
    @submit="handleSubmit"
    >
    <FormKit
        name="ignore"
        v-model="check_box_value"
        type="checkbox"
        label="Safety features"
        :options="check_box_labels"
    />
    <FormKit
        name="Size_Class"

        type="select"
        label="Choose a vehicle class:"
        :options="class_options"
    />
    <FormKit
      name="Curb_Wgt"
      label="Enter the curb weight of the vehicle (lbs):"
      type="number"
      step="0.01"
    />
    <FormKit
      name="SSF"
      label="Please enter the static stability factor:"
      type="number"
      step="0.01"
    />
    <FormKit
      name="TireSize"
      label="Please enter the size of the tires:"
      type="number"
      step="0.01"
    />
    <FormKit
      name="WheelsDriven"
      label="Please enter the number of wheels driven:"
      type="number"
    />
    <FormKit
        name="Drive_type"

        type="select"
        label="Choose a drive type:"
        :options="drive_options"
    />
    </FormKit>
</template>