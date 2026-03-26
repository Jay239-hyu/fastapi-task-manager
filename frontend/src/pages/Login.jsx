// ===================== Login.jsx (Polished) =====================
import { useState } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const nav = useNavigate();

  const login = async () => {
    try {
      setLoading(true);
      setError("");

      const res = await API.post("/auth/login", { username, password });
      localStorage.setItem("token", res.data.access_token);
      nav("/dashboard");
    } catch (err) {
      setError("Invalid username or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-800">
      <div className="bg-slate-800 p-8 rounded-2xl w-80 shadow-xl">
        <h2 className="text-white text-2xl mb-6 font-semibold">Welcome Back 👋</h2>

        {error && (
          <p className="text-red-400 text-sm mb-3">{error}</p>
        )}

        <input
          className="w-full p-2 mb-3 rounded bg-slate-700 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="password"
          className="w-full p-2 mb-4 rounded bg-slate-700 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={login}
          disabled={loading}
          className="w-full bg-indigo-500 p-2 rounded text-white hover:bg-indigo-600 transition disabled:opacity-50"
        >
          {loading ? "Logging in..." : "Login"}
        </button>
      </div>
    </div>
  );
}
