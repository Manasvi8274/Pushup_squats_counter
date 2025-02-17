export const startPushups = () => {
    console.log("pushups count started")
    fetch("http://localhost:8000/start_pushups")
    };
export const stopPushups = () => {
    console.log("pushups count stopped")
    fetch("http://localhost:8000/stop_pushups")
    };
export const startSquats = () =>{
    console.log("squats count started")
    fetch("http://localhost:8000/start_squats")
    };
export const stopSquats = () =>{
    console.log("squats count stopped")
    fetch("http://localhost:8000/stop_squats")
    };
export const resetCounts = () =>{
    console.log("reset sucessfully")
    fetch("http://localhost:8000/reset")
    };
