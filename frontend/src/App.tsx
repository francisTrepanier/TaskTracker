import { useState } from 'react'
import './App.css'

type Task = {
  title: string
  notes: string
  completed: boolean
  id: number
  created_at: string | Date
}

function App() {
  const [tasks, setTasks] = useState<Task[]>([])

  const fetchTasks = async () => {
    try {
      const response = await fetch('http://localhost:8000/tasks')
      const backendTasks: Task[] = await response.json()
      setTasks((backendTasks))
    } catch (error) {
      console.error('Failed to fetch tasks', error)
    }
  }

  const addTmpTask = () => setTasks((tasks) => [...tasks,
  {
    title: "test",
    notes: `Task ${tasks.length + 1}`,
    completed: false,
    id: tasks.length + 1,
    created_at: new Date()
  }])

  return (
    <>
      <section id="center">
        <button type="button" className="counter" onClick={addTmpTask}>
          add temp test task
        </button>
        <button type="button" className="task-button" onClick={fetchTasks}>
          fetch tasks from backend
        </button>
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              [{task.id}] -
              {task.title}:{task.notes} -
              {task.completed ? "✅" : "❌"} -
              {(task.created_at instanceof Date ? task.created_at : new Date(task.created_at)).toLocaleString()}
            </li>
          ))}
        </ul>
      </section>


      <div className="ticks"></div>
      <section id="spacer"></section>
      <p>
        Edit <code>src/App.tsx</code> and save to test <code>HMR</code>
      </p>
    </>
  )
}

export default App
