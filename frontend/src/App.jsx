import React,{useEffect,useState} from "react";
import {LineChart,Line,XAxis,YAxis,Tooltip,ResponsiveContainer} from "recharts";

const API="http://localhost:8000";
export default function App(){
 const [latest,setLatest]=useState(null),[history,setHistory]=useState([]),[aqi,setAqi]=useState(null),[pred,setPred]=useState(null),[error,setError]=useState("");
 async function load(){
  try{
   const [a,b,c,d]=await Promise.all([
    fetch(API+"/api/readings/latest").then(r=>r.json()),
    fetch(API+"/api/readings?limit=24").then(r=>r.json()),
    fetch(API+"/api/aqi").then(r=>r.json()),
    fetch(API+"/api/predictions").then(r=>r.json())
   ]);
   setLatest(a);setHistory(b.map((x,i)=>({...x,name:i+1})));setAqi(c);setPred(d);setError("");
  }catch(e){setError("Backend is not running. Start FastAPI on port 8000.");}
 }
 useEffect(()=>{load();const t=setInterval(load,5000);return()=>clearInterval(t)},[]);
 return <main>
  <header><div><h1>Air Quality Monitor</h1><p>IoT + AI Pollution Monitoring Dashboard</p></div><span className="live">● LIVE</span></header>
  {error&&<div className="error">{error}</div>}
  <section className="cards">
   <Card title="PM2.5" value={latest?latest.pm25:"--"} unit="µg/m³"/>
   <Card title="PM10" value={latest?latest.pm10:"--"} unit="µg/m³"/>
   <Card title="Temperature" value={latest?latest.temperature:"--"} unit="°C"/>
   <Card title="Humidity" value={latest?latest.humidity:"--"} unit="%"/>
   <Card title="AQI Status" value={aqi?aqi.category:"--"} unit=""/>
  </section>
  <section className="panel"><h2>PM2.5 History</h2><div className="chart"><ResponsiveContainer width="100%" height="100%"><LineChart data={history}><XAxis dataKey="name"/><YAxis/><Tooltip/><Line type="monotone" dataKey="pm25" strokeWidth={3}/></LineChart></ResponsiveContainer></div></section>
  <section className="bottom">
   <div className="panel"><h2>AI Prediction</h2><p className="prediction">{pred?pred.next_pm25:"--"} µg/m³</p><p>Predicted {pred?.horizon||""}</p><small>{pred?.model||""}</small></div>
   <div className="panel"><h2>Latest Reading</h2><p>{latest?new Date(latest.timestamp).toLocaleString():"--"}</p><p>CO₂: {latest?.co2??"--"} ppm</p></div>
  </section>
 </main>
}
function Card({title,value,unit}){return <div className="card"><span>{title}</span><strong>{value}</strong><small>{unit}</small></div>}
