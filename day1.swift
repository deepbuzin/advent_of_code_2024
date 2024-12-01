import Foundation

do {
    let inputString = try String(contentsOfFile: "input_day1.txt", encoding: .utf8)
    let lines = inputString.split(separator: "\n")

    let columns = lines.map { line -> (Int?, Int?) in
        let vals = line.split(separator: "   ")
        return (Int(vals[0]), Int(vals[1]))
    }

    let leftColumn = columns.compactMap({ $0.0 })
    let rightColumn = columns.compactMap({ $0.1 })

    let distance = zip(leftColumn.sorted(), rightColumn.sorted()).reduce(0) {
        result, vals in
        let (left, right) = vals
        return result + abs(left - right)
    }

    print(distance)

    var counts: [Int: Int] = [:]

    for right in rightColumn {
        counts[right, default: 0] += 1
    }

    let similarity = leftColumn.reduce(0) { result, left in
        result + left * counts[left, default: 0]
    }

    print(similarity)

} catch {
    print("\(error)")
}
