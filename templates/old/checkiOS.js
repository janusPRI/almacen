function iOS() {
  return [
    'iPad Simulator',
    'iPhone Simulator',
    'iPod Simulator',
    'iPad',
    'iPhone',
    'iPod'
  ].includes(navigator.platform)
  // iPad on iOS 13 detection
  || (navigator.userAgent.includes("Mac") && "ontouchend" in document)
}

function iOSold() {
  let iOSlist=[
    'iPad Simulator',
    'iPhone Simulator',
    'iPod Simulator',
    'iPad',
    'iPhone',
    'iPod'
  ]
  return (iOSlist.indexOf(navigator.platform)>=0)

  // iPad on iOS 13 detection
  // || (navigator.userAgent.includes("Mac") && "ontouchend" in document)
}

function iOSlink(){
   if(iOS()){
    var iOSlink = document.getElementById("id-iOSlink");
    iOSlink.innerHTML= "Si usas un iPhone mirá el catálogo en este link";
  }

}

// window.addEventListener('load', iOSlink () )