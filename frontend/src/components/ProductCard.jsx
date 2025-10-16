// src/components/ProductCard.jsx
export default function ProductCard({ product, onRecommend }) {
  return (
    <div className="bg-white rounded-xl shadow hover:shadow-xl overflow-hidden transition-all">
      <img
        src={product.image || "https://via.placeholder.com/300x200"}
        alt={product.title}
        className="h-48 w-full object-cover"
      />
      <div className="p-4">
        <h3 className="text-lg font-semibold text-gray-900">{product.title}</h3>
        <p className="text-sm text-gray-500 mb-2">{product.category}</p>
        <p className="text-lg font-bold text-yellow-600 mb-4">
          ₹{product.price.toFixed(2)}
        </p>
        <button
          onClick={() => onRecommend(product.id)}
          className="w-full bg-yellow-500 hover:bg-yellow-600 text-gray-900 font-semibold py-2 rounded-md"
        >
          Get Recommendations
        </button>
      </div>
    </div>
  );
}
