import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import ProductCard from "../components/ProductCard";
import RecommendationCard from "../components/RecommendationCard";
import { API_BASE_URL } from "../config";

export default function Home() {
  const [products, setProducts] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch(`${API_BASE_URL}/products`)
      .then((res) => res.json())
      .then(setProducts)
      .catch(console.error);
  }, []);

  const handleRecommend = async (id) => {
    setLoading(true);
    setRecommendations([]);

    try {
      const res = await fetch(`${API_BASE_URL}/recommend`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ product_id: id }),
      });
      const data = await res.json();
      setRecommendations(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <div className="p-8 max-w-7xl mx-auto">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">
          Popular Products
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {products.map((p) => (
            <ProductCard key={p.id} product={p} onRecommend={handleRecommend} />
          ))}
        </div>

        {loading && (
          <p className="text-center text-gray-600 mt-8">
            Fetching recommendations...
          </p>
        )}

        {recommendations.length > 0 && (
          <div className="mt-12">
            <h2 className="text-2xl font-bold mb-4 text-gray-800">
              Recommended For You
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
              {recommendations.map((r, i) => (
                <RecommendationCard key={i} rec={r} />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
