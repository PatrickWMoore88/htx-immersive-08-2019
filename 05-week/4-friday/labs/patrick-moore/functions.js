// TimeIntervals
var timeIntervals = [ 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000];

// Randomizer Function
function randomizer(arr){
    var currentIndex = arr.length, temporaryValue, randomIndex;
    while( 0 !== currentIndex){
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = arr[currentIndex];
        arr[currentIndex] = arr[randomIndex];
        arr[randomIndex] = temporaryValue;
    }
    return arr[0]
}
// Randomizer Variables
var randomTimeInterval = randomizer(timeIntervals);
`
// StopWatch
console.log("Starting StopWatch:")
var stopWatch = new Promise(function(resolve){
    setTimeout(function(){
        resolve("It took this long: " + (randomTimeInterval / 1000) + " seconds.");
    }, randomTimeInterval);
});

stopWatch.then(function(value){
    console.log(value);
})

// The Tortoise And The Hare
console.logLater = (message, delay) => setTimeout(function() {
    console.log(message);
  }, delay);
console.log("Ready")
console.logLater("Set", 1000);
console.logLater("Go!", 2000);
var tortoise = new Promise(function(resolve){
    setTimeout(resolve, randomTimeInterval, "Tortoise Wins! At a Time of: " + (randomTimeInterval / 1000) + " seconds!");
});
var hare = new Promise(function(resolve){
    setTimeout(resolve, randomTimeInterval, "Hare Wins! At a Time of: " + (randomTimeInterval / 1000) + " seconds!");
});

Promise.race([tortoise, hare]).then(function(value){
    console.logLater(value, 2000);
});`

// Logger Function
