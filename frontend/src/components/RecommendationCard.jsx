// src/components/RecommendationCard.jsx
export default function RecommendationCard({ rec }) {
  return (
    <div className="bg-gray-800 text-white rounded-xl shadow p-4 hover:scale-105 transition-all">
      <img
        src={rec.image || "https://via.placeholder.com/300x200"}
        alt={rec.title}
        className="h-40 w-full object-cover rounded-md mb-3"
      />
      <h4 className="font-semibold">{rec.title}</h4>
      <p className="text-sm text-gray-400">{rec.category}</p>
      <p className="font-bold text-yellow-400 mt-1">₹{rec.price.toFixed(2)}</p>
    </div>
  );
}
