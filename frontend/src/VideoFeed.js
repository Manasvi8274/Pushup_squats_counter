import React, { useEffect, useState } from "react";

function VideoFeed({ setPushups, setSquats }) {
    const [image, setImage] = useState(null); // Start with null instead of ""

    useEffect(() => {
        const socket = new WebSocket("ws://localhost:8000/ws");
        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.image) {
                setImage(`data:image/jpeg;base64,${data.image}`);
                setPushups(data.pushups);
                setSquats(data.squats);
            }
        };
        return () => socket.close();
    }, []);

    return (
        <div>
            {image ? (
                <img src={image} alt="Webcam Feed" style={{ width: "500px", height: "auto" }} />
            ) : (
                <p>Loading video feed...</p>
            )}
        </div>
    );
}

export default VideoFeed;
