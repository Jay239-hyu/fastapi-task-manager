// ===================== Dashboard.jsx (Polished) =====================
import { useEffect, useState } from "react";
import API from "../api";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");
  const [loading, setLoading] = useState(false);

  const loadTasks = async () => {
    const res = await API.get("/tasks");
    setTasks(res.data);
  };

  const createTask = async () => {
    if (!title) return;

    setLoading(true);
    await API.post("/tasks", {
      title,
      description: desc,
      is_completed: false,
    });
    setTitle("");
    setDesc("");
    await loadTasks();
    setLoading(false);
  };

  const deleteTask = async (id) => {
    await API.delete(`/tasks/${id}`);
    loadTasks();
  };

  const toggle = async (t) => {
    await API.put(`/tasks/${t.id}`, {
      ...t,
      is_completed: !t.is_completed,
    });
    loadTasks();
  };

  useEffect(() => {
    loadTasks();
  }, []);

  return (
    <div className="flex h-screen bg-slate-900 text-white">

      {/* Sidebar */}
      <div className="w-60 bg-slate-950 p-6">
        <h2 className="text-lg mb-6 font-semibold">⚡ AI Tasks</h2>
        <div className="space-y-3">
          <p className="bg-slate-800 p-2 rounded">Dashboard</p>
          <p className="p-2 text-gray-400">AI Tools</p>
        </div>
      </div>

      {/* Main */}
      <div className="flex-1 p-8">

        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-semibold">Dashboard</h2>
          <button
            onClick={() => {
              localStorage.clear();
              location.href = "/";
            }}
            className="bg-red-500 px-4 py-1 rounded hover:bg-red-600 transition"
          >
            Logout
          </button>
        </div>

        {/* Add Task */}
        <div className="bg-slate-800 p-5 rounded-xl mb-6 shadow-md">
          <input
            className="w-full p-2 mb-2 bg-slate-700 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500"
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <input
            className="w-full p-2 mb-3 bg-slate-700 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500"
            placeholder="Description"
            value={desc}
            onChange={(e) => setDesc(e.target.value)}
          />
          <button
            onClick={createTask}
            disabled={loading}
            className="bg-indigo-500 px-4 py-2 rounded hover:bg-indigo-600 transition disabled:opacity-50"
          >
            {loading ? "Adding..." : "Add Task"}
          </button>
        </div>

        {/* Tasks */}
        {tasks.length === 0 ? (
          <p className="text-gray-400">No tasks yet. Add your first task 🚀</p>
        ) : (
          <div className="space-y-4">
            {tasks.map((t) => (
              <div
                key={t.id}
                className="bg-slate-800 p-4 rounded-xl flex justify-between items-center shadow hover:shadow-lg transition"
              >
                <div>
                  <h4 className={t.is_completed ? "line-through text-gray-400" : ""}>
                    {t.title}
                  </h4>
                  <p className="text-sm text-gray-400">{t.description}</p>
                </div>

                <div className="space-x-2">
                  <button
                    onClick={() => toggle(t)}
                    className="bg-green-500 px-3 rounded hover:bg-green-600 transition"
                  >
                    ✓
                  </button>
                  <button
                    onClick={() => deleteTask(t.id)}
                    className="bg-red-500 px-3 rounded hover:bg-red-600 transition"
                  >
                    ✕
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}

      </div>
    </div>
  );
}
