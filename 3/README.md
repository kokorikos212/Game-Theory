
# Nash Equilibria & Correlated Equilibria Computation using Nashpy

## 🧠 Description

This project computes all **Nash equilibria** and at least one **correlated equilibrium** (that is **not** a Nash equilibrium) for a given bimatrix game using:

- The **Lemke–Howson algorithm**
- The **support enumeration method**
- A **linear program** that finds correlated equilibria

The algorithms are applied using the [nashpy](https://github.com/drvinceknight/nashpy) library, and standard optimization tools from `scipy.optimize`.

---

## 📌 Exercise Instructions

> Χρησιμοποιήστε την βιβλιοθήκη `nashpy` ώστε να υπολογίσετε όλα τα σημεία ισορροπίας Nash του παιγνίου που δίνεται στην ΄Ασκηση 1. Να χρησιμοποιήσετε τόσο τον αλγόριθμο **Lemke–Howson** όσο και τον αλγόριθμο **απαρίθμησης φορέα**.  
> Στη συνέχεια, να προγραμματίσετε ένα **γραμμικό πρόγραμμα** που να επιστρέφει τουλάχιστον **ένα συσχετισμένο σημείο ισορροπίας**, το οποίο **να μην είναι σημείο ισορροπίας Nash**.

---

## 🔍 Nash Equilibria

We compute Nash equilibria using two methods:

### 1. Lemke–Howson

```python
game.lemke_howson(initial_dropped_label=label)
```

This is repeated for different labels to collect all reachable equilibria.

### 2. Support Enumeration

```python
for eq in game.support_enumeration():
    print(eq)
```

---

## 🔗 Correlated Equilibrium (Not a Nash)

We solve a **linear program** to find a correlated equilibrium \( p(i,j) \) that satisfies:

- All joint probabilities sum to 1
- Incentive constraints for both players
- At least one inequality is **strict** (ensuring it's **not** a Nash equilibrium)

### 🎯 LP Formulation Highlights

- Variables:  
  \( x = 	ext{flattened vector of } p(i,j) \) (length \( n^2 \))

- Equality constraint:  
  \( \sum_{i,j} p(i,j) = 1 \)

- Inequality constraints:
  - For all \( i 
eq i' \):  
    \[
    \sum_j p(i,j)(A[i,j] - A[i',j]) \geq 0
    \]
  - For all \( j 
eq j' \):  
    \[
    \sum_i p(i,j)(B[i,j] - B[i,j']) \geq 0
    \]

- Non-negativity: \( p(i,j) \geq 0 \)

### Code

See the notebook for the full LP-based implementation using `scipy.optimize.linprog`.

---

## 🛠 Requirements

- `numpy`
- `scipy`
- `nashpy`
- `matplotlib` (optional, for visualizations)

Install them via pip:

```bash
pip install numpy scipy nashpy matplotlib
```

---

## ✅ Example Output

```bash
Nash Equilibria:
  (array([1., 0., 0.]), array([0., 1., 0.]))
  ...

Correlated Equilibrium (not Nash):
[[0.3 0.2 0. ]
 [0.1 0.1 0.1]
 [0.  0.1 0.1]]
```

---

## 📁 File Structure

```
├── equilibrium_computation.ipynb
├── README.md
```

---

## 📚 References

- [Nashpy documentation](https://nashpy.readthedocs.io/)
- Osborne & Rubinstein: *A Course in Game Theory*
- Hart & Mas-Colell: *A Simple Adaptive Procedure Leading to Correlated Equilibrium*

---

## 👨‍🔬 Author

Applied Mathematics student project – exploring equilibrium concepts via computation.
