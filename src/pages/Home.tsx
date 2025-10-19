import { useState } from 'react'

export const Home = () => {
  const [tasks, setTasks] = useState<string[]>([])
  const [inputValue, setInputValue] = useState('')

  const handleAddTask = () => {
    if (inputValue.trim() === '') return
    setTasks([...tasks, inputValue])
    setInputValue('')
  }

  return (
    <div className='flex flex-col items-center justify-center min-h-screen bg-gray-100'>
      <h1
        className='text-4xl font-bold text-blue-600'
        data-testid='main-header'
        id='home-title'
      >
        My To-Do App
      </h1>

      <div className='flex gap-2 mb-4'>
        <input
          id='task-input'
          type='text'
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder='Enter a task'
          className='border rounded px-3 py-2 w-64'
        />
        <button
          id='add-task-btn'
          onClick={handleAddTask}
          className='bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700'
        >
          Add
        </button>
      </div>

      <ul id='task-list' className='w-64'>
        {tasks.map((task, index) => (
          <li key={index} className='border-b py-2'>
            {task}
          </li>
        ))}
      </ul>
    </div>
  )
}
