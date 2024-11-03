#include <DHT.h>

#define DHTPIN 23     // Pino onde o DHT22 está conectado
#define DHTTYPE DHT22 // Tipo do sensor DHT

#define LDR_PIN 34 // Pin do LDR

#define POTASSIO_PIN 21
#define FOSFORO_PIN 22

#define RELAY_PIN 5   // Pino do relé


DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  Serial.println("FarmTech Solutions.");
  dht.begin();

  pinMode(LDR_PIN, INPUT);
  pinMode(POTASSIO_PIN, INPUT);
  pinMode(FOSFORO_PIN, INPUT);

  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW); // Começa com o relé desligado

}

void loop() {
  delay(2000);

  int potassio = digitalRead(POTASSIO_PIN);
  int fosforo = digitalRead(FOSFORO_PIN);
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int ldrValue = analogRead(LDR_PIN);

  // Mapear o valor do LDR para a escala de pH (0 a 14)
  float phValue = map(ldrValue, 0, 4095, 0, 14);
  
  Serial.print("Potássio (K): "); Serial.println(potassio);
  Serial.print("Fósforo (P): "); Serial.println(fosforo);
  Serial.print("Umidade: "); Serial.print(humidity); Serial.println("%");
  Serial.print("Temperatura: "); Serial.print(temperature); Serial.println("°C");
  Serial.print("Ph: "); Serial.println(phValue);

  bool needIrrigation = false;

  // Regras de irrigação
  if (humidity < 30 || potassio == LOW || fosforo == LOW || phValue < 6.0) {
    needIrrigation = true;
  }

  if (needIrrigation) {
    digitalWrite(RELAY_PIN, HIGH); // Liga a bomba d'água
    Serial.println("Bomba ligada: Iniciando irrigação.");
  } else {
    digitalWrite(RELAY_PIN, LOW); // Desliga a bomba d'água
    Serial.println("Bomba desligada: Solo em condições ideais.");
  }

  Serial.println("CRUD Python: \n");
  
  Serial.println("" + String(humidity) + "," + String(temperature) + "," + String(fosforo) + "," + String(potassio) + "," + String(phValue) + "," + String(needIrrigation));
}