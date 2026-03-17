"use client";

import { useState } from "react";
import { queryAPI } from "../lib/api";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    const res = await queryAPI(input);
    setResponse(res.response);
  };

  return (
    <div>
      <textarea
        rows={4}
        style={{ width: "100%" }}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
      <pre>{response}</pre>
    </div>
  );
}