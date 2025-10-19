export const Home = () => {
  return (
    <div className='flex flex-col items-center justify-center min-h-screen bg-gray-100'>
      <h1
        className='text-4xl font-bold text-blue-600'
        data-testid='main-header'
        id='home-title'
      >
        My To-Do App
      </h1>
      <p className='text-gray-600 mt-2'>
        Welcome! Manage your tasks efficiently 🚀
      </p>
    </div>
  )
}
