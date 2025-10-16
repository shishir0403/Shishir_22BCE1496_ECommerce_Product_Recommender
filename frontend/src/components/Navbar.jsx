// src/components/Navbar.jsx
export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white px-6 py-4 flex items-center justify-between shadow-lg">
      <div className="text-2xl font-bold tracking-tight text-yellow-400">
        🛒 ShopSmart
      </div>

      <div className="flex-1 mx-8">
        <input
          type="text"
          placeholder="Search for products..."
          className="w-full px-4 py-2 rounded-md bg-gray-800 text-gray-200 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        />
      </div>

      <div className="flex items-center space-x-4">
        <button className="bg-yellow-500 hover:bg-yellow-600 px-4 py-2 rounded-md font-semibold text-gray-900">
          Login
        </button>
      </div>
    </nav>
  );
}
