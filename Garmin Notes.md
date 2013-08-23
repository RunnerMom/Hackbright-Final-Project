122c0d49084cdac2edd20cc2da166b3d

<script type="text/javascript"> 
   function load() {
      var display = new Garmin.DeviceDisplay("garminDisplay", { 
         pathKeyPairsArray: ["http://10.1.10.24:5000",
                             "122c0d49084cdac2edd20cc2da166b3d"],
         autoFindDevices: true, //start searching for devices
         showStatusElement: true, //basic feedback provided
         showReadDataElement: false, //don't offer to read data
         //add other options per the documentation  
      });
   }    
</script>   
