# 🧠 Ανάλυση Ακτινογραφιών για Διάγνωση COVID-19 με Χρήση Βαθιάς Μάθησης

## 📌 Περιγραφή

Αυτό το υποσύστημα αποτελεί μέρος ενός ολοκληρωμένου έργου βαθιάς μάθησης με στόχο τη **διάγνωση ασθενειών από ακτινογραφίες θώρακα**. Το μοντέλο που αναπτύσσεται ταξινομεί τις ακτινογραφίες σε τρεις κατηγορίες:

- ✅ Υγιής (Healthy)
- 🦠 Ασθενής με COVID-19
- 🌫️ Ασθενής με κοινή πνευμονία

Χρησιμοποιεί σύγχρονες τεχνικές της τεχνητής νοημοσύνης και βασίζεται σε προ-εκπαιδευμένα μοντέλα όπως το **VGG16**.

---

## 🚀 Τεχνολογίες

- Python
- **TensorFlow & Keras** (deep learning)
- **OpenCV** (επεξεργασία εικόνας)
- **Pandas & NumPy** (χειρισμός δεδομένων)
- **Matplotlib** (οπτικοποίηση)
- **Google Colab / Google Drive** – Εκτέλεση και αποθήκευση


---

## ⚙️ Λειτουργίες

### 1. Προεπεξεργασία Δεδομένων

- **Κανονικοποίηση** των εικόνων (rescaling σε [0,1]).
- **Data Augmentation** με χρήση `ImageDataGenerator`:
  - Περιστροφή, μετατοπίσεις, ζουμ, shear.
  - Μείωση overfitting με αλλαγές στις εικόνες.
- Διαχωρισμός των δεδομένων σε **training** και **validation set** με ισορροπημένες κατηγορίες.


### 2. Δημιουργία Μοντέλου

- Βασισμένο στο **VGG16** με βάρη από ImageNet (`include_top=False`).
- Τα αρχικά layers του μοντέλου **παγώνουν** για να διατηρηθούν οι προκαθορισμένες γνώσεις.
- Προστίθενται πλήρως συνδεδεμένα layers (Dense) και dropout για αποφυγή overfitting.
- Τελικό layer με **softmax** για τριπλή κατηγοριοποίηση.

### 3. Εκπαίδευση & Αξιολόγηση

- Ορισμός batch size, αριθμού εποχών, validation split
- Υποστήριξη **συνέχισης εκπαίδευσης** από προϋπάρχον μοντέλο (`load_weights`)
- Χρήση callbacks όπως `ModelCheckpoint`, `ReduceLROnPlateau`
   - ModelCheckpoint: Αποθήκευση του καλύτερου μοντέλου με βάση τη val_accuracy.
   - ReduceLROnPlateau: Αυτόματη μείωση learning rate αν δεν βελτιώνεται η απόδοση.
   - LearningRateScheduler: Σταδιακή αλλαγή του learning rate.
   - Custom Monitoring Callback: Εκτύπωση πληροφοριών ανά εποχή, χρόνος εκτέλεσης και διαφορά val_acc - acc.
- Ρύθμιση Learning Rate Scheduling με συνάρτηση lr_schedule (μείωση του ρυθμού όσο αυξάνονται οι εποχές εκπαίδευσης)
- Υπολογισμός accuracy, precision, recall 

### 4. Αποθήκευση & Αναφορά

- Αποθήκευση εκπαιδευμένων μοντέλων σε φάκελο `saved_models_VGG16validation`
- Οπτικοποίηση αποτελεσμάτων με διαγράμματα
   - Γραφήματα Loss vs Val Loss
     
     <p align="left">
      <img src="https://github.com/haris2718/Deep_learning_covid/blob/main/assets/Loss.png" width="25%" hspace="10" />  
     </p>
     
   - Γραφήματα Accuracy vs Val Accuracy
     <p align="left">
      <img src="https://github.com/haris2718/Deep_learning_covid/blob/main/assets/Accuracy.png" width="25%" hspace="10" />  
     </p>
- Αποθήκευση αποτελεσμάτων σε `.csv`

---

## 📁 Δομή Δεδομένων

```bash
project/
├── extracted_files/
│   ├── train_images/              # Εικόνες εκπαίδευσης
│   ├── labels_train.csv           # Ετικέτες για το train set
│   └── saved_models_VGG16validation/
│       └── <αποθηκευμένα_μοντέλα>.h5


