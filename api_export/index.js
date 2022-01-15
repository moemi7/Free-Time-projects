const express = require('express')
const request = require('request-promise')

const app = express();
const PORT = process.env.PORT || 5000;
//const land = `duitsland`
const apiKey = '3d900b3eba7c9c9d50351b0be9b377b1'
//const baseUrl = `https://www.nederlandwereldwijd.nl/landen/${land}/reizen/reisadvies`;

app.use(express.json());

app.get('/500', (req,res) => {
    res.send('Welcom');
});
app.get('/landen/:land', async (req,res)=> {
const { land } = req.params;
    
 
const response = await request(`https://www.nederlandwereldwijd.nl/landen/${land}/reizen/reisadvies`);
var matches1 = response.match(/oranje/);
var matches2 = response.match(/rood/);
var matches3 = response.match(/groen/);
var count1 = (response.match(/oranje/g) || []).length;
var count2 = (response.match(/groen/g) || []).length;
var count3 = (response.match(/rood/g) || []).length;
var count4 = (response.match(/geel/g) || []).length;
let c = ``;

var b = ``;

console.log(`${matches1}+${matches2}+${matches3}+${count1}`)

if (matches1 != null){
    b = matches1;
    
}
else if(matches2 != null){
    b = matches2;
}
else if(matches3 != null){
    b = matches3;
}
if (count1 > count2 && count1 > count3 && count1 > count4){
    c = `oranje`;
}
else if (count2 > count1 && count2 > count3 && count2 > count4){
    c = `groen`;
}
else if (count3 > count2 && count3 > count1 && count3 > count4){
    c = `rood`;
}
else if (count4 > count2 && count4 > count1 && count4 > count3){
    c = `geel`;
}
else{
    c=`geen een dayumm`;
}


console.log(`${b}+${c}`)
});

app.listen(PORT, () => console.log(`rwina ${PORT}`));