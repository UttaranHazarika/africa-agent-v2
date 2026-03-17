export async function queryAPI(query) {
  const res = await fetch(
    process.env.NEXT_PUBLIC_API_URL + "/query",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query })
    }
  );

  return res.json();
}