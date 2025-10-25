"use client";

import { useState, useEffect } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/history")
      .then(res => res.json())
      .then(data => setHistory(data))
      .catch(err => console.error("Error fetching history:", err));
  }, []);

  const handleAnalyze = async () => {
    const res = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    console.log("API result:", data);

    setResult(data);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Guard AI Dashboard</h1>

      <textarea
        rows="4"
        placeholder="Enter Amharic or English text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{ width: "100%", marginBottom: "1rem" }}
      />
      <button onClick={handleAnalyze}>Analyze</button>

      {result && (
        <div style={{ marginTop: "1rem" }}>
          <h3>Result:</h3>
          <p><b>Label:</b> {result.label}</p>
<p><b>Score:</b> {result.score ? result.score.toFixed(3) : "N/A"}</p>
        </div>
      )}

      <h2>History</h2>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>ID</th>
            <th>Text</th>
            <th>Label</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {history.map((row) => (
            <tr key={row.id}>
              <td>{row.id}</td>
              <td>{row.text}</td>
              <td>{row.label}</td>
              <td>{row.score?.toFixed(3)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
