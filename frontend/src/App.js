import React, { useState, useEffect } from "react";
import VideoFeed from "./VideoFeed";
import { startPushups, stopPushups, startSquats, stopSquats, resetCounts } from "./api";

function App() {
  const [pushups, setPushups] = useState(0);
  const [squats, setSquats] = useState(0);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Push-up & Squat Counter</h1>
      <VideoFeed setPushups={setPushups} setSquats={setSquats} />
      <p>Push-ups: {pushups}</p>
      <p>Squats: {squats}</p>
      <button onClick={startPushups}>Start Push-ups</button>
      <button onClick={stopPushups}>Stop Push-ups</button>
      <button onClick={startSquats}>Start Squats</button>
      <button onClick={stopSquats}>Stop Squats</button>
      <button onClick={resetCounts}>Reset</button>
    </div>
  );
}

export default App;
