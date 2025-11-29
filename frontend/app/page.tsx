export default function Home() {
  return (
    <div style={{padding: "40px", fontFamily: "Arial", textAlign: "center"}}>
      <h1 style={{fontSize: "48px", color: "#006233"}}>سمعة DZ 🇩🇿</h1>
      <p style={{fontSize: "24px"}}>راقب اسم شركتك في كل الأخبار الجزائرية فورًا</p>
      <input 
        type="text" 
        placeholder="اكتب اسم الشركة (مثل: سوناطراك، كوندور، سيفيتال)" 
        style={{padding: "15px", width: "500px", fontSize: "20px", margin: "20px"}}
      />
      <button style={{padding: "15px 30px", fontSize: "20px", background: "#006233", color: "white", border: "none"}}>
        ابحث الآن
      </button>
      <p style={{marginTop: "50px"}}>النسخة التجريبية مجانية 100% لأول 100 شركة جزائرية</p>
    </div>
  )
}
