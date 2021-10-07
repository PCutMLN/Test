var nama="Abiyyu";
var umur=14;
var lakilaki=true
if(!lakilaki){
    console.log("saya perempuan");
}   else {
    console.log("saya laki-laki");
}
var daftarnama=[
    "Abiyyu",
    "Abi",
    "Biyu",
]
var panjang=daftarnama.length
daftarnama.push("tambahan")
console.log(daftarnama[3])

for (var i=0; i<5; i++) {
    console.log(i+" loop")
}
var i=0;
while (i<5) {
    console.log(i+" loop2");
    i++
}
var j=5
var loop = true
while (loop){
    j--;
    console.log(loop +" "+j+" loop2");
    if(j<0) {
        loop=false;
    }
}
// FUNCTION
function add(a,b){
    return a+b;
}
// VARIABLE
// 1. declaration & assignment
var hasil1=add(1,3);
console.log(hasil1);
// 2. assignment
var hasil1=add(2,5);
console.log(hasil1);
var tambah=function(a,b){
    return a+b;
}
// 3. declaration only
hasil1=kali(2,5);
console.log(hasil1);
hasil1=kali(3,6);
console.log(hasil1);
// loop luar 1
// i = 0
// false
// hasil *

// loop luar 2
// i=1
// j=0;  true; star = "**"
// j=1: false
// hasil **
for (var i=0;i<5;i++ ) {
    var star="*"
    for(var j=0;j<1;j++) {
        star=star+"*";
    }
    console.log(star);
}